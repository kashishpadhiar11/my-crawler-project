# Web Crawler Project (Internship Assignment)

This repository contains my internship assignment submission, which includes:

- ✅ Website crawling logic
- ✅ English sentence extraction and transformation into 20 variations
- ✅ CSV pipeline with structured outputs
- ✅ Modular Python code
- ✅ Working CLI interface (optional if implemented)

---

## What Didn't Work (Airflow)

I attempted to configure Apache Airflow to orchestrate the crawling pipeline, but hit the following blockers:

- Airflow refused to detect my DAG, despite the correct `AIRFLOW__CORE__DAGS_FOLDER` configuration.
- `daily_gnosis_dag.py` either failed silently or didn't show up due to parsing issues.
- Import errors from Airflow’s example DAGs cluttered the logs.
- Time constraints during setup and debugging (plus Airflow’s aggressive UX) made it impractical to resolve in time.

> 💡 Despite this, the core functionality of the project works independently of Airflow. The crawler logic and outputs can still be run manually or integrated into any job scheduler (e.g. `cron`, `Prefect`, `Dagster` etc).

---

## Setup

```bash
git clone https://github.com/kashishpadhiar11/my-crawler-project.git
cd my-crawler-project
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt