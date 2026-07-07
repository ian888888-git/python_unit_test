from src.pipeline import ProductionPipeline

def bootstrap(self) -> None:
    pipeline =  ProductionPipeline()
    pipeline.start()

if __name__ == "__main__":
    bootstrap()