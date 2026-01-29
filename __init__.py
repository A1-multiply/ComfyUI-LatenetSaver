from .latent_saver import (
    A1_Save_Latent,
    A1_Load_Latent,
)

NODE_CLASS_MAPPINGS = {
    "A1SaveLatent": A1_Save_Latent,
    "A1LoadLatent": A1_Load_Latent,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "A1SaveLatent": "A1 Save Latent",
    "A1LoadLatent": "A1 Load Latent",
}
