import shutil
from pathlib import Path

PROCESSED = Path("data/processed")
ANALYTICS = Path("data/analytics")
DATALAKE = Path("data/datalake")

def export_folder(src: Path, dst: Path):
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    print(f"✔ Exportado: {src} → {dst}")

def main():
    print("Exportando dados para o Data Lake local...")

    DATALAKE.mkdir(parents=True, exist_ok=True)

    export_folder(PROCESSED, DATALAKE / "processed")
    export_folder(ANALYTICS, DATALAKE / "analytics")

    print("\n✔ Sprint 5 concluída: Data Lake atualizado em data/datalake/")

if __name__ == "__main__":
    main()
