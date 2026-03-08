# Schemas Module – Recurrent Language Model with LangGraph

This module contains *data validation and serialization schemas* used across the API, pipelines, and graph workflows. The schemas ensure consistent and type‑safe data structures between request inputs, internal workflows, and model output representations.

## Overview

The `app/schemas` directory houses Pydantic models and type definitions for:

- API request and response payloads  
- Internal data structures passed through pipelines  
- Graph state and node input/output formats  
- Embeddings and retrieval results  

These schemas provide central, reusable definitions that make the application safe, clear, and predictable.

---

## Core Idea

Schemas provide *type‑safe data contracts* between components such as:

- API handlers and clients  
- Ingestion pipelines and vector stores  
- Language model workflows and graph engines  
- Metrics and tracing modules

Pydantic validation ensures malformed or unexpected data is rejected early, improving reliability and debugging.

---

## System Capabilities

### Request & Response Schemas

- Define input shapes for API endpoints  
- Validate required fields and types  
- Enforce constraints for text, metadata, and query parameters

### Internal Workflow Schemas

- Standardize document chunks  
- Model embedding records  
- Track retrieval result formats

### Graph State Models

- Represent LangGraph state objects  
- Declare shared properties across nodes  
- Ensure typed access in graph workflows

### Output Schemas

- Structured model outputs  
- Consistent cross‑pipeline formats  
- Include metadata such as timestamps, relevance, and IDs

---

## Key Schema Types

Schemas typically include:

- **Prompt and query request models**  
- **Document and chunk formats**  
- **Embedding and vector store record definitions**  
- **Graph state and node I/O models**  
- **Inference response and metadata wrappers**

Schemas are based on Pydantic (v2+) for strict type enforcement, serialization, and introspection.

---

## High‑Level Example

```python
from pydantic import BaseModel

class InferenceRequest(BaseModel):
    question: str
    context: str | None = None

class InferenceResponse(BaseModel):
    answer: str
    source_ids: list[str] = []
    timestamp: str
```
## Design Principles

- **Type safety first** – Ensures reliable data contracts  
- **Reusability** – Same schemas are used across API, pipelines, and graph logic  
- **Clear boundaries** – Separates data validation from logic  
- **Consistent serialization** – Same format for persistence and messaging  

---

## Workflow Summary

- API layer receives input and parses with request schemas  
- Pipelines and internal components use consistent data formats  
- Graph workflows operate on typed state objects  
- Model outputs are formatted with response schemas  
- Clients receive predictable, validated JSON structures  

---

## Technology Stack

| Component | Technology |
|-----------|------------|
| Language | Python |
| Validation | Pydantic (v2+) |
| Type Hints | Python type system |
| Serialization | Pydantic BaseModel |

---

## Intended Use Cases

- Validating API inputs and outputs  
- Enforcing internal data structures through workflows  
- Supporting typed graph state for LangGraph executions  
- Centralizing data definitions for maintainability  

---

## License

This module is part of the Recurrent Language Model with LangGraph project, licensed under the MIT License.
