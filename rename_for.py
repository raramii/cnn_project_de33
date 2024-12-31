import os

# 파일이 있는 디렉토리 경로
folder_path = r"C:\Workspaces\cnn_project\car\Validation\Truck\RMC"  # 변경할 경로로 수정

# 폴더 내 모든 파일을 정렬해서 가져옴
files = os.listdir(folder_path)

# 파일 이름을 순차적으로 변경
for index, filename in enumerate(files, start=1):  # 1부터 시작
    # 파일 경로 (경로는 그대로 두고, 파일명만 변경)
    old_file_path = folder_path + "\\" + filename  # 경로 구분자를 직접 처리
    
    # '-숫자.jpg'로 끝나는 파일을 찾음
    if filename.endswith(".jpg"):
        # '트럭_트레일러-' 이후 숫자를 제거하고, Trailer_1.jpg 형식으로 변경
        # 예시: 트럭_트레일러-1.jpg -> Trailer_1.jpg
        new_filename = f"RMC_{index}.jpg"
        
        new_file_path = folder_path + "\\" + new_filename  # 경로 구분자를 직접 처리
        
        # 파일명 변경
        os.rename(old_file_path, new_file_path)
        print(f"파일명이 '{filename}'에서 '{new_filename}'로 변경되었습니다.")
