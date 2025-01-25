import torch
import torch.nn as nn

# 모델 정의
class MNISTModel(nn.Module):
    def __init__(self):
        super(MNISTModel, self).__init__()
        self.fc1 = nn.Linear(28 * 28, 128) # 입력: 28*28=784, 출력: 128
        self.fc2 = nn.Linear(128, 64) # 입력: 128, 출력: 64
        self.fc3 = nn.Linear(64, 10) # 입력: 64, 출력: 10 (10개의 클래스)

    def forward(self, x):
        x = x.view(-1, 28 * 28) # 배치 크기와 상관없이 1D 텐서로 변환
        x = torch.relu(self.fc1(x)) # ReLU활성화 함수
        x = torch.relu(self.fc2(x)) # ReLU활성화 함수
        x = self.fc3(x) # 최종 출력
        return x
    
# 모델 불러오기 함수
def load_model(model_path):
    model = MNISTModel() # 모델 인스턴스 생성
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu'))) # 모델 가중치 로드
    model.eval() # 모델을 평가 모드로 전환
    return model