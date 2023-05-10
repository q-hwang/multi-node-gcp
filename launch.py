from google.cloud import aiplatform

project_id = 'hai-gcp-model-medical'
location = 'us-central1'
bucket_name = 'medfm_job'

args = [
    "--dataset_name", "wikitext",
    "--dataset_config_name", "wikitext-2-raw-v1",
    "--model_name_or_path", "gpt2",
    "--output_dir", "gs://medfm_data/output",
]


package_uri = f'gs://{bucket_name}/tmp.tar.gz'
python_module = 'trainer.train'
machine_type = 'n1-standard-4'
accelerator_count = 1
accelerator_type = 'NVIDIA_TESLA_T4'
worker_pool_specs =  [{
    "machine_spec": {
        "machine_type": machine_type,
        "accelerator_type": accelerator_type,
        "accelerator_count": accelerator_count,
    },
    "replica_count": 1,
    "python_package_spec": {
        "executor_image_uri": "us-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-7:latest",
        "package_uris": [package_uri],
        "python_module": python_module,
        "args": args,
        # "script": "train.sh",
    },   
},
{
    "machine_spec": {
        "machine_type": machine_type,
        "accelerator_type": accelerator_type,
        "accelerator_count": accelerator_count,
    },
    "replica_count": 1,
    "python_package_spec": {
        "executor_image_uri": "us-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-7:latest",
        "package_uris": [package_uri],
        "python_module": python_module,
        "args": args,
        # "script": "train.sh",
    },   
},
]

aiplatform.init(project=project_id, location=location)

job = aiplatform.CustomJob(
    display_name='my-custom-job',
    worker_pool_specs=worker_pool_specs,
    staging_bucket=bucket_name,
)

job.run(sync=True)