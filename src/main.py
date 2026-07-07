from src.pipeline import ProductionPipeline

def bootstrap() -> None:
    pipeline =  ProductionPipeline()
    pipeline.start()

if __name__ == "__main__":
    bootstrap()