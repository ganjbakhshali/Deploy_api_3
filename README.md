# FastAPI Seven Sins

This FastAPI application provides endpoints to learn about and visualize the seven symbolic items associated with the Persian New Year tradition of Haft-Seen (Seven S's).

## Overview

Haft-Seen, meaning "Seven S's," is a traditional Persian custom observed during Nowruz, the Iranian New Year. It involves setting a table with seven symbolic items, each starting with the Persian letter "سین" (S).

This FastAPI application serves information about the seven items and their symbolic meanings. Additionally, it provides images of each item.

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
    ```

## Usage

Run the FastAPI application using the following command:

```bash
uvicorn main:app --reload
```
The API will be available at http://localhost:8000.

# Endpoints
* /: Root endpoint providing an introduction to Haft-Seen.
* /sins: Endpoint listing the names of the seven items.
* /sins/{sin_name}: Endpoint providing descriptions of individual items. Replace {sin_name} with the name of the item (e.g., sib, senjed).
* /sins/{sin_name}/image: Endpoint providing images of individual items. Replace {sin_name} with the name of the item (e.g., sib, senjed).