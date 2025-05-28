## Entity-Relationship Overview

```
ConnectorConfig            PlatformProduct
     |                            |
     v                            v
PlatformCustomer ----< PlatformOrder >--- OrderItem
     |                     |
     v                     v
RecommendationLog     RefundRequest
                            |
AddressUpdateRequest    

TryOnSession --< TryOnOverlay
```

---

## 1. `ConnectorConfig`

Stores credentials & sync settings for each platform.

| Column          | Type              | Constraints                     | Description                   |
| --------------- | ----------------- | ------------------------------- | ----------------------------- |
| `id`            | UUID              | PK, default `gen_random_uuid()` | Config record ID              |
| `platform`      | VARCHAR(50)       | NOT NULL                        | Enum: 'shopify','woocommerce' |
| `api_key`       | VARCHAR(255)      | NOT NULL                        | API key or OAuth token        |
| `secret`        | VARCHAR(255)      | NOT NULL                        | API secret (encrypted)        |
| `store_url`     | VARCHAR(255)      | NOT NULL                        | Store domain/endpoint         |
| `sync_interval` | INT               | NOT NULL, default 300           | Poll interval in seconds      |
| `created_at`    | TIMESTAMP WITH TZ | NOT NULL, default now()         | Creation timestamp            |
| `updated_at`    | TIMESTAMP WITH TZ | NOT NULL, default now()         | Last update timestamp         |

---

## 2. `PlatformProduct`

Unified product catalog across platforms.

| Column        | Type              | Constraints            | Description                     |
| ------------- | ----------------- | ---------------------- | ------------------------------- |
| `sku`         | VARCHAR(100)      | PK                     | Unique SKU across all platforms |
| `platform`    | VARCHAR(50)       | PK                     | Enum: 'shopify','woocommerce'   |
| `title`       | VARCHAR(255)      | NOT NULL               | Product title                   |
| `description` | TEXT              |                        | Product description             |
| `metadata`    | JSONB             |                        | Raw platform-specific payload   |
| `price`       | DECIMAL(10,2)     | NOT NULL               | Price                           |
| `available`   | BOOLEAN           | NOT NULL, default TRUE | Stock availability              |
| `synced_at`   | TIMESTAMP WITH TZ |                        | Last sync timestamp             |

Indexes:

* PK on (`sku`,`platform`)
* Index on `available`

---

## 3. `PlatformCustomer`

Stores customer profiles from each platform.

| Column        | Type              | Constraints | Description                   |
| ------------- | ----------------- | ----------- | ----------------------------- |
| `customer_id` | VARCHAR(100)      | PK          | Platform-specific customer ID |
| `platform`    | VARCHAR(50)       | PK          | Enum: 'shopify','woocommerce' |
| `email`       | VARCHAR(255)      | NOT NULL    | Email address                 |
| `name`        | VARCHAR(255)      |             | Full name                     |
| `metadata`    | JSONB             |             | Raw platform-specific data    |
| `synced_at`   | TIMESTAMP WITH TZ |             | Last sync timestamp           |

Indexes:

* PK on (`customer_id`,`platform`)
* Index on `email`

---

## 4. `PlatformOrder`

Order header information.

| Column         | Type              | Constraints                         | Description                   |
| -------------- | ----------------- | ----------------------------------- | ----------------------------- |
| `order_id`     | VARCHAR(100)      | PK                                  | Platform-specific order ID    |
| `platform`     | VARCHAR(50)       | PK                                  | Enum: 'shopify','woocommerce' |
| `customer_id`  | VARCHAR(100)      | FK → `PlatformCustomer.customer_id` | Customer placing the order    |
| `status`       | VARCHAR(50)       | NOT NULL                            | Order lifecycle status        |
| `total_amount` | DECIMAL(10,2)     | NOT NULL                            | Total paid                    |
| `currency`     | VARCHAR(10)       | NOT NULL                            | Currency code                 |
| `line_items`   | JSONB             | NOT NULL                            | Items array as raw payload    |
| `created_at`   | TIMESTAMP WITH TZ | NOT NULL, default now()             | Order creation timestamp      |
| `synced_at`    | TIMESTAMP WITH TZ |                                     | Last sync timestamp           |

Indexes:

* PK on (`order_id`,`platform`)
* Index on `customer_id`

---

## 5. `OrderItem`

Normalized order items for analytics & recommendations.

| Column     | Type          | Constraints                     | Description                 |
| ---------- | ------------- | ------------------------------- | --------------------------- |
| `id`       | UUID          | PK, default `gen_random_uuid()` | Internal surrogate key      |
| `order_id` | VARCHAR(100)  | FK → `PlatformOrder.order_id`   | Parent order ID             |
| `platform` | VARCHAR(50)   | FK → `PlatformOrder.platform`   | Platform                    |
| `sku`      | VARCHAR(100)  |                                 | Product SKU                 |
| `quantity` | INT           | NOT NULL, default 1             | Quantity ordered            |
| `price`    | DECIMAL(10,2) | NOT NULL                        | Unit price at time of order |

Indexes:

* Index on (`order_id`,`platform`)

---

## 6. `RefundRequest`

Tracks refund automation.

| Column         | Type              | Constraints                     | Description                          |
| -------------- | ----------------- | ------------------------------- | ------------------------------------ |
| `id`           | UUID              | PK, default `gen_random_uuid()` | Request ID                           |
| `order_id`     | VARCHAR(100)      | FK → `PlatformOrder.order_id`   | Order being refunded                 |
| `platform`     | VARCHAR(50)       |                                 | Platform                             |
| `status`       | VARCHAR(50)       | NOT NULL                        | Enum: 'pending','processed','failed' |
| `response`     | JSONB             |                                 | Platform API response                |
| `requested_at` | TIMESTAMP WITH TZ | NOT NULL, default now()         | Timestamp                            |

Indexes:

* Index on `status`

---

## 7. `AddressUpdateRequest`

Logs address change attempts.

| Column         | Type              | Constraints                     | Description                        |
| -------------- | ----------------- | ------------------------------- | ---------------------------------- |
| `id`           | UUID              | PK, default `gen_random_uuid()` | Request ID                         |
| `order_id`     | VARCHAR(100)      | FK → `PlatformOrder.order_id`   | Order to update                    |
| `platform`     | VARCHAR(50)       |                                 | Platform                           |
| `new_address`  | JSONB             | NOT NULL                        | Address payload                    |
| `status`       | VARCHAR(50)       | NOT NULL                        | Enum: 'pending','updated','failed' |
| `response`     | JSONB             |                                 | Platform API response              |
| `requested_at` | TIMESTAMP WITH TZ | NOT NULL, default now()         | Timestamp                          |

---

## 8. `RecommendationLog`

Records recommendations served.

| Column            | Type              | Constraints                         | Description                        |
| ----------------- | ----------------- | ----------------------------------- | ---------------------------------- |
| `id`              | UUID              | PK, default `gen_random_uuid()`     | Log entry ID                       |
| `customer_id`     | VARCHAR(100)      | FK → `PlatformCustomer.customer_id` | Customer receiving recommendations |
| `recommendations` | TEXT\[]           | NOT NULL                            | List of SKU strings                |
| `confidence`      | DECIMAL(5,2)      |                                     | Average confidence score (%)       |
| `requested_at`    | TIMESTAMP WITH TZ | NOT NULL, default now()             | Timestamp                          |

Indexes:

* Index on `customer_id`
* Index on `requested_at`

---

## 9. `TryOnSession`

Manages virtual try-on interactions.

| Column        | Type              | Constraints                                   | Description                                        |
| ------------- | ----------------- | --------------------------------------------- | -------------------------------------------------- |
| `session_id`  | UUID              | PK, default `gen_random_uuid()`               | Session ID                                         |
| `customer_id` | VARCHAR(100)      | FK → `PlatformCustomer.customer_id`, nullable | Optional link to known customer                    |
| `selfie_url`  | TEXT              | NOT NULL                                      | Stored selfie image URL                            |
| `status`      | VARCHAR(50)       | NOT NULL, default 'created'                   | Enum: 'created','in\_progress','complete','failed' |
| `created_at`  | TIMESTAMP WITH TZ | NOT NULL, default now()                       | Timestamp                                          |

---

## 10. `TryOnOverlay`

Stores results of product overlays.

| Column        | Type              | Constraints                     | Description             |
| ------------- | ----------------- | ------------------------------- | ----------------------- |
| `id`          | UUID              | PK, default `gen_random_uuid()` | Overlay record ID       |
| `session_id`  | UUID              | FK → `TryOnSession.session_id`  | Parent try-on session   |
| `sku`         | VARCHAR(100)      | NOT NULL                        | SKU overlaid            |
| `overlay_url` | TEXT              | NOT NULL                        | Generated composite URL |
| `created_at`  | TIMESTAMP WITH TZ | NOT NULL, default now()         | Timestamp               |

---
