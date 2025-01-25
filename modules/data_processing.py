import torchvision.transforms as transforms
from PIL import Image
import io

# 이미지 전처리 함수
def transform_image(image):
    # 이미지를 28x28로 리사이즈하고 텐서로 변환
    image = image.resize((28, 28)) # MLP 모델이 기대하는 입력 크기로 리사이즈
    image = transforms.ToTensor()(image) # Tensor로 변환
    image = image.unsqueeze(0) # 배치 차원 추가 (1, 1, 28, 28)
    return image

# 전처리 함수를 통해 텐서 크기를 (1, 1, 28, 28)로 만듬 
#   - 첫 번째 차원 (1): 배치 크기 (한 번에 입력되는 이미지의 개수)
#   - 두 번째 차원 (1): 채널 (그레이스케일이므로 채널 수가 1)
#   - 세 번째 차원 (28): 높이
#   - 네 번째 차원 (28): 너비
