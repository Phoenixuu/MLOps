from zenml.steps import step
from zenml.pipelines import pipeline

@step
def data_preprocessing() -> dict:
	data = {
	"text": ["Coding C++ is the best", "Python is trash", "DesignPattern is important"],
	"labels": [1,0,1]
	}
	return data

@step
def train_model(data: dict) -> str:
	print(f"Training on data: {data['text']}")
	return "Trained sentiment model"

@pipeline
def sentiment_analysis_pipeline(data_preprocessing, train_model):
	data = data_preprocessing()
	model = train_model(data)

sentiment_pipeline = sentiment_analysis_pipeline(
	data_preprocessing = data_preprocessing(),
	train_model = train_model()
)

sentiment_pipeline.run()