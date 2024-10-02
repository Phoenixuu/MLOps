import click
from pipelines.training_pipeline import ml_pipeline
from zenml.integrations.mlflow.mlflow_utils import get_tracking

@click.command()
def main():
	"""
	Run the ML pipeline and start the LMflow UI for experiment
	"""
	#Run the pipeline
	run = ml_pipeline()

	#customize
	trained_model = run["model_building_step"]
	print(f"Trianed Model Type: {type(trained_model)}")

	print(
		"Now run \n"
		f"	mlflow ui --backend--store-uri '{get_tracking_uri}"
		)