
import fiftyone as fo
import fiftyone.brain as fob # ML routines
dataset = fo.load_dataset("pboxGufeng")
fob.compute_similarity(
    dataset,
    brain_key="zero_shot_simofa",
    model="zero-shot-classification-transformer-torch",
    embeddings="ofaemb",
    name_or_path="OFA-Sys/chinese-clip-vit-base-patch16",
)

