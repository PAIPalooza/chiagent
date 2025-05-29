### Epic 1: Connector Scaffold

**Goal:** Stand up the modules and routes for Shopify & WooCommerce connectors.

| Story ID | User Story                                                                                     | Acceptance Criteria                                                            |
| -------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| CONN-1   | As a developer, I want to model the `ConnectorConfig` table so that credentials can be stored. | Migration runs, `connector_config` table exists with all defined columns.      |
| CONN-2   | As a developer, I want to scaffold Shopify connector module so that we have a placeholder.     | `/connect/shopify` route exists and returns 200 with `{ status: "stub" }`.     |
| CONN-3   | As a developer, I want to scaffold WooCommerce connector so that we can add auth later.        | `/connect/woocommerce` route exists and returns 200 with `{ status: "stub" }`. |

---

### Epic 2: Product Discovery

**Goal:** Implement data model and a stubbed search endpoint to return sample product data.

| Story ID | User Story                                                                                            | Acceptance Criteria                                                               |
| -------- | ----------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| PROD-1   | As a developer, I want to create the `PlatformProduct` model so that products can be stored.          | Migration runs, `platform_product` table exists with defined schema.              |
| PROD-2   | As a developer, I want to build a basic sync-job stub for one platform so that we have sample rows.   | A background task or endpoint seeds at least one sample `PlatformProduct` record. |
| PROD-3   | As a shopper, I want `GET /search?q=any` to return sample products so I can verify endpoint behavior. | Hitting `/search?q=test` returns a JSON array with at least one product object.   |

---

### Epic 3: Customer Service Stub

**Goal:** Provide stub endpoints for refunds and address updates that log incoming payloads.

| Story ID | User Story                                                                                              | Acceptance Criteria                                                                   |
| -------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| CS-1     | As a visitor, I want `POST /orders/{orderId}/refund` stubbed so that I can see request payload logged.  | Calling the endpoint logs the body to console/DB and returns `{ status: "pending" }`. |
| CS-2     | As a visitor, I want `POST /orders/{orderId}/address` stubbed so that I can see request payload logged. | Calling the endpoint logs the body to console/DB and returns `{ status: "pending" }`. |

---

### Epic 4: Virtual Try-On Stub

**Goal:** Scaffold selfie session creation and product overlay stubs with placeholder URLs.

| Story ID | User Story                                                                                                           | Acceptance Criteria                                                                      |
| -------- | -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| TRY-1    | As a user, I want `POST /tryon/sessions` to return a new `sessionId` and dummy `selfieUrl` so I can start a session. | Endpoint returns `{ sessionId: "<uuid>", selfieUrl: "https://placeholder.selfie.jpg" }`. |
| TRY-2    | As a user, I want `POST /tryon/{sessionId}/product/{sku}` to return a mock overlay so I can verify the flow.         | Endpoint returns `{ overlayUrl: "https://placeholder.overlay.jpg" }`.                    |

---

### Epic 5: Demo & Retrospective

**Goal:** Validate prototypes and capture next steps.

| Story ID | User Story                                                                                       | Acceptance Criteria                                                                          |
| -------- | ------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------- |
| DEMO-1   | As a team lead, I want to demo all stubbed endpoints so stakeholders can see progress.           | Each endpoint (`/connect/*`, `/search`, `/orders/*`, `/tryon/*`) responds as expected.       |
| RETRO-1  | As a team, I want to document blockers and next action items so we have clear post-sprint tasks. | A short list of at least 3 follow-up tasks is recorded in the project board or sprint notes. |

---

**Total Stories:** 14
**Estimated Time per Story:** \~4 min each (some parallelizable by two devs)


