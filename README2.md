# ComfyUI LatentSaver

A custom node for ComfyUI that allows you to **save and reload latent values after the Sampling stage**  
in image and video generation workflows.  
Its main purpose is to prevent workflow interruptions caused by **VRAM Out of Memory (OOM)** errors during the Decode stage.

---

After Sampling, the latent is saved.  
Even if ComfyUI needs to be restarted, the saved latent can be loaded again and directly connected to Decode.  
The overall workflow is shown below.

![Sample Node](img/Sample_node.png)

---

Latents generated after Sampling are saved using the **Save Latent** node into the output folder.

- Latents are always saved **relative to the output folder**
- File names and subfolder names can be **freely customized**
- Path and name changes are allowed **only inside the output folder**

Example of saving a latent:

![Save Latent Example](img/Save_latent_example.png)

---

Saved latents can be restored using the **Load Latent** node.

- When loading, **all latent files under the output folder are automatically scanned**
- You do not need to remember the exact save path
- All subfolders under output are searched, making reconnection much simpler

Example of loading a saved latent and reconnecting it to Decode:

![Load Latent Example](img/load_latent_example.png)

---

A common problem in video generation workflows looks like this:

1. Sampling completes successfully  
2. **VRAM Out of Memory (OOM)** occurs during the Decode stage  
3. ComfyUI exits and the workflow is interrupted  

With LatentSaver, the workflow becomes:

1. Save the latent immediately after Sampling  
2. OOM occurs during Decode  
3. Restart ComfyUI  
4. Load the previously saved latent  
5. Connect it directly to Decode and continue from the last result  

There is no need to re-run Sampling.  
Previously computed results are preserved,  
allowing you to continue working without losing progress due to VRAM issues.

---

This node provides the following functionality:

- Save Latent  
- Load Latent  

Latents are always saved and loaded relative to the output folder.  
The subfolder structure under output can be freely organized.  
Saved latents remain available even after restarting ComfyUI.  
This node is especially useful in environments with limited VRAM.

---

A1
