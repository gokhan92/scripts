#python bqtoGcs.py --region $REGIONENVVAR --runner DataflowRunner --project $PROJECTENVVAR --service_account_email $SERVICEACCOUNTENVVAR --subnetwork $SUBNETWORKENVVAR

import apache_beam as beam
from apache_beam.options import pipeline_options
from apache_beam.options.pipeline_options import SetupOptions
import google.auth

from apache_beam.runners import DataflowRunner
import argparse
import logging
from apache_beam.io.gcp.internal.clients import bigquery
from apache_beam.runners.interactive.interactive_runner import InteractiveRunner
import apache_beam.runners.interactive.interactive_beam as ib

output_file = "gs://bucketsTotest92/tmp/test"


class SelectColumns(beam.DoFn):
	def process(self, element):
		return[{*element.items()}]
	
def run(argv=None):
	parser = argparse.ArgumentParser()
	#Adding custom  arguments 
	parser.add_argument("--runner", dest='runner', default='', help="Specify which runner to use")
	parser.add_argument("--project", dest='project', default='', help="GCP project ID if DataflowRunner is used")
	parser.add_argument("--region", dest='region', default='', help="GCP region if DataflowRunner is used")
	parser.add_argument("--service_account_email", dest='service_account_email', default='', help="GCP Service Account-Id: $SERVICEACCOUNTVARIABLE if DataflowRunner is used")
	parser.add_argument("--subnetwork", dest='subnetwork', default='', help="GCP Subnet used either $GKESUBNETVARIABLE")
	parser.add_argument("--no_use_public_ips", dest='no_use_public_ips', default=None, help="Issue to fix quota errors")
	parser.add_argument("--machine_type", dest='machine_type', default='', help="dataflow worker machine types")
	parser.add_argument("--job_name", dest='job_name', default='TESTING', help="Job name")
	
	args = parser.parse_args()
	
	google_options = [
	'--job_name=test-bqtoGcs',
	f'--runner={args.runner}',
	f'--project={args.project}',
	f'--region={args.region}',
	f'--service_account_email={args.service_account_email}',
	f'--subnetwork={args.subnetwork}',
	'--no_use_public_ips',
	'--machine_type=n1-standard-1',
	'--staging_location=gs://bucketsTotest92/tmp/staging',
	'--temp_location=gs://bucketsTotest92/tmp',
	]
	options = pipeline_options.PipelineOptions(google_options)
	testQuery = "SELECT *  from `projectId.datasetName.test2` "
	
	with beam.Pipeline(options=options) as p:
		results = (
					p
					| 'Read Account Hardship View Query' >> beam.io.ReadFromBigQuery(query = testQuery, use_standard_sql = True,
                     project='projectId',
                     temp_dataset=bigquery.DatasetReference(
          projectId='projectId', datasetId='datasetId'))                                                               
					# Each row is a dictionary where the keys are the BigQuery columns
					| 'Select columns' >> beam.ParDo(SelectColumns())
					| 'Save to bucket' >> beam.io.WriteToText(output_file, file_name_suffix=".txt")

		)

if __name__=="__main__":
	logging.getLogger().setLevel(logging.INFO)
	run()
