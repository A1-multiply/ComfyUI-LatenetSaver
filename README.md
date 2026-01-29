# ComfyUI LatentSaver
Save & Load Latents to Avoid VRAM OOM in ComfyUI

---

## Overview

ComfyUI LatentSaver는 영상/이미지 생성 워크플로에서  
Sampling 이후 생성된 Latent 값을 저장하고 다시 불러오기 위한 노드입니다.

주 용도는 Decode 단계에서 VRAM 부족(OOM)으로 작업이 터지는 상황을 방지하는 것입니다.

---

## Sample Workflow

아래 이미지는 전체적인 노드 흐름 예시입니다.  
Sampling 이후 Latent를 저장하고, ComfyUI 재시작 후 다시 불러와 Decode에 연결하는 구조입니다.

![Sample Node](img/Sample_node.png)

---

## Save Latent (저장)

Save Latent 노드는 Sampling 이후 생성된 Latent 값을 output 폴더에 저장합니다.

- Latent는 항상 output 폴더에 저장됩니다
- 파일 이름과 하위 폴더 이름은 자유롭게 수정할 수 있습니다
- 단, output 폴더 내부에서만 경로 및 이름 수정이 가능합니다

저장 예시는 아래와 같습니다.

![Save Latent Example](img/Save_latent_example.png)

Latent는 output 폴더 하위에 사용자가 지정한 폴더와 이름으로 저장됩니다.

---

## Load Latent (불러오기)

Load Latent 노드는 output 폴더 하위에 존재하는 모든 latent 파일을 자동으로 검색합니다.

- 저장된 정확한 경로를 기억할 필요가 없습니다
- output 폴더 아래에 있는 모든 하위 폴더를 탐색하여 latent 파일을 찾아줍니다
- 저장된 latent를 다시 연결하는 과정이 훨씬 간단해집니다

저장된 Latent를 다시 불러와 Decode에 연결하는 예시는 아래와 같습니다.

![Load Latent Example](img/load_latent_example.png)

---

## Why this node exists (VRAM OOM 해결)

영상 생성 작업에서 자주 발생하는 문제 흐름은 다음과 같습니다.

Sampling까지는 정상적으로 완료되지만  
Decode 단계에서 VRAM Out of Memory(OOM)가 발생하면서  
ComfyUI가 종료되고 작업이 중단됩니다.

LatentSaver를 사용하면 다음과 같이 작업할 수 있습니다.

Sampling 완료 후 Latent를 미리 저장하고  
Decode 단계에서 OOM이 발생하더라도  
ComfyUI를 재시작한 뒤  
Load Latent로 이전 Latent를 불러와  
Decode에 바로 연결하여 이전 결과를 그대로 이어서 확인할 수 있습니다.

Sampling을 다시 돌릴 필요 없이  
지금까지 열받던 VRAM 문제를 깔끔하게 해결할 수 있습니다.

---

## Installation

ComfyUI의 custom_nodes 폴더에 이 저장소를 클론한 후  
ComfyUI를 재시작하면 됩니다.

---

## Nodes

- Save Latent  
- Load Latent  

---

## Notes

- Latent는 항상 output 폴더 기준으로 저장 및 로드됩니다
- output 폴더 내부의 하위 폴더 구조는 자유롭게 구성할 수 있습니다
- ComfyUI 재시작 후에도 저장된 Latent는 유지됩니다
- VRAM이 작은 환경에서 특히 유용합니다

---

## Author

A1
