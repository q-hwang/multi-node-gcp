

JOB_NAME="test"
REGION="us-central1"



# submit training job to Vertex Training with 
# pre-built container using gcloud CLI
# gcloud beta ai custom-jobs create \
gcloud ai custom-jobs create \
    --display-name=${JOB_NAME} \
    --region ${REGION} \
    --worker-pool-spec=replica-count=1,machine-type='n1-standard-4',accelerator-type='NVIDIA_TESLA_T4',accelerator-count=2,executor-image-uri=us-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-7:latest,script='train.sh',local-package-path="trainer/"\
    --worker-pool-spec=replica-count=1,machine-type='n1-standard-4',accelerator-type='NVIDIA_TESLA_T4',accelerator-count=2



#  --worker-pool-spec=replica-count=1,machine-type='n1-standard-4',accelerator-type='NVIDIA_TESLA_T4',accelerator-count=4,executor-image-uri=us-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-7:latest,script='train.sh',local-package-path="trainer/" \

# python setup.py sdist
# gsutil cp dist/*.tar.gz gs://medfm_job/tmp.tar.gz
# python launch.py 