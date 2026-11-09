# ✍️ Automated Blog & Content Harvester Pipeline

> A high-performance web crawling engine engineered to parse blog archives, extract editorial titles, contributor metadata, and taxonomy tags, and serialize clean records directly into structured Excel spreadsheets (`.xlsx`). Built for SEO analysts, content aggregators, and automated research workflows.

---

## 🏗️ Pipeline Architecture
---

## 🧰 Technical Stack

- **Core Runtime:** Python 3.10+
- **HTTP Transport:** `requests` (with timeout and error handling handlers)
- **DOM Parsing:** `BeautifulSoup4` (HTML markup traversal)
- **Data Manipulation:** `pandas` (DataFrame memory mapping)
- **Spreadsheet Engine:** `openpyxl` (Office Open XML serialization)

---

## ⚡ Engineering Highlights

1. **🛡️ Resilient Multi-Page Crawling:** Dynamically loops through paginated blog endpoints with built-in HTTP exception catching to prevent pipeline crashes.
2. **🧹 Text Normalization & Flattening:** Automatically strips dirty whitespace, extracts taxonomy lists, and formats them into clean comma-separated strings.
3. **⚡ In-Memory Data Buffering:** Processes scraped dictionaries directly inside high-speed pandas dataframes prior to final disk flush.

---

## ⚙️ Quick Start & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/blog-content-harvester.git](https://github.com/your-username/blog-content-harvester.git)
   cd blog-content-harvester
