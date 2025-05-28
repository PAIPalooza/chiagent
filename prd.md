## 1. Executive Summary

Deliver an AI-driven Customer Agent that integrates with Shopify and WooCommerce to:

* Assist shoppers in product discovery via natural-language queries and faceted search.
* Automate customer service tasks (refunds, pre‑fulfillment address changes).
* Provide personalized recommendations based on past purchase history.
* Enable a virtual try-on experience using Google AI Mode via selfie uploads.
* Expose a unified RESTful API and support MCP protocol for easy embedding in front-end and third‑party systems.

---

## 2. Goals & Objectives

1. **Conversion Uplift**: Guide users to products matching their intent quickly.
2. **Support Efficiency**: Reduce manual ticketing by automating common post-purchase actions.
3. **Engagement**: Increase dwell time and satisfaction via virtual try-on.
4. **Ease of Integration**: Provide out-of-the-box connectors for Shopify & WooCommerce with minimal setup.

---

## 3. MVP Scope

### In Scope

* **Platform Connectors**: Sync products, orders, and customers from Shopify and WooCommerce via their public APIs.
* **Product Discovery**: NL query parsing → faceted search (category, price, attributes) over unified catalog.
* **Customer Service Actions**:

  * **Refunds**: `POST /orders/{orderId}/refund` → trigger platform refund.
  * **Address Updates**: `POST /orders/{orderId}/address` (pre‑shipment only).
* **Recommendations**: Analyze historical orders per customer → `GET /customers/{custId}/recommendations`.
* **Virtual Try-On**:

  * Selfie upload: `POST /tryon/sessions`
  * Overlay SKU: `POST /tryon/{sessionId}/product/{sku}` → Google AI Mode API invocation.
* **API & MCP**: REST endpoints + MCP-compliant JSON interface.

### Out of Scope

* Connectors for platforms beyond Shopify & WooCommerce.
* Post-delivery address changes.
* Deep front-end UI implementations (API consumers will handle UX).

---

## 4. User Personas

| Persona       | Need                                                       |
| ------------- | ---------------------------------------------------------- |
| Shopper       | Rapid discovery, virtual try-on, self‑service support      |
| Support Agent | Minimal manual interventions; clear action logs            |
| Merchandiser  | Insights on customer interests for merchandising decisions |
| Developer     | Simple connector configuration; reliable, documented APIs  |

---

## 5. Functional Requirements

### 5.1 Platform Connectors

* **Shopify** & **WooCommerce**:

  * Credential management (OAuth/API key).
  * Scheduled sync or webhook subscription for:

    * **Products**: `id`, `title`, `description`, `images`, `price`, `tags`, `variants`.
    * **Customers**: `id`, `email`, `name`.
    * **Orders**: `id`, `customer_id`, `line_items`, `status`.

### 5.2 Product Discovery

* **NL Query Endpoint**: `GET /search?q={text}&filters={json}` → returns top N SKUs with metadata.
* **Facets**: support filterable fields (category, price ranges, tags).

### 5.3 Customer Service Automation

* **Refund**:

  * `POST /orders/{orderId}/refund` → platform API call; returns refund status.
* **Address Update**:

  * `POST /orders/{orderId}/address` → validate `Order.status == 'created'`; update via platform API; log audit.

### 5.4 Recommendations

* **Ingestion**: Collect order history on sync.
* **Algorithm**: Simple collaborative filtering or rule-based “also bought” logic.
* **Endpoint**: `GET /customers/{custId}/recommendations?limit=5` → list of SKUs + confidence.

### 5.5 Virtual Try-On

* **Session Creation**:

  * `POST /tryon/sessions` body: `selfie` (base64/URL) → returns `sessionId` + `selfieUrl`.
* **Product Overlay**:

  * `POST /tryon/{sessionId}/product/{sku}` → fetch product asset; call Google AI Mode; return composite image URL.

### 5.6 API & MCP Protocol

* **RESTful**: JSON-over-HTTP; standard status codes.
* **MCP Compatibility**: Wrap requests/responses in MCP JSON envelopes for LLM integrations.

---

## 6. Technical Architecture & Stack

* **API Server**: Node.js (Express) or Python (FastAPI).
* **Database**: PostgreSQL for relational data; Redis for session caching.
* **Sync Workers**: Celery/RabbitMQ or serverless functions for connector jobs.
* **AI Services**: Google AI Mode API for image overlays; optional LLM (OpenAI) for NL parsing.
* **Hosting**: Docker on Kubernetes/ECS.

---

## 7. Data Model Highlights

* **PlatformProduct**: `sku`, `title`, `platform`, `metadata` (JSON).
* **PlatformCustomer**: `customerId`, `email`, `platform`.
* **PlatformOrder**: `orderId`, `status`, `customerId`, `items` (JSON).
* **TryOnSession**: `sessionId`, `selfieUrl`, `createdAt`.
* **RecommendationLog**: `customerId`, `recommendations`, `timestamp`.

---

## 8. Milestones & Timeline

| Phase                 | Duration | Deliverables                                                               |
| --------------------- | -------- | -------------------------------------------------------------------------- |
| 1. Connector Setup    | 2 weeks  | OAuth/API key flows; product/order/customer sync for Shopify & WooCommerce |
| 2. Discovery & Search | 2 weeks  | NL query parsing; faceted search; endpoint QA                              |
| 3. Service Actions    | 2 weeks  | Refund and address-update workflows; audit logging                         |
| 4. Recommendations    | 2 weeks  | History ingestion; recommendation endpoint                                 |
| 5. Virtual Try-On     | 2 weeks  | Selfie session; overlay endpoint; performance testing                      |
| 6. MCP & API Docs     | 1 week   | MCP protocol support; SDK/docs; sample integration                         |

---
