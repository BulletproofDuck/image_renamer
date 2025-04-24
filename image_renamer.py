# -*- coding: utf-8 -*-
import os
from pathlib import Path
import tkinter.messagebox as msgbox
import time

def main():
    print("ㅎㅇ\n변경할 이미지들이 있는 폴더 경로를 입력하세요:")
    folder_input = input("예: D:\\cyoa\\amalgam\\character\n> ").strip()

    print("\n새 파일 이름 형식을 입력하세요 (예: 캐릭터) (뒤쪽에 (-001)이런식으로 번호가 붙습니다.):")
    name_input = input("> ").strip()

    print("\n정렬 기준을 선택하세요:")
    print("1: 이름순")
    print("2: 수정된 날짜순")
    sort_choice = input("번호 입력 (1 또는 2): ").strip()

    print("\n정렬 방향을 선택하세요:")
    print("1: 오름차순 (예: 오래된 → 최신)")
    print("2: 내림차순 (예: 최신 → 오래된)")
    order_choice = input("번호 입력 (1 또는 2): ").strip()

    folder = Path(folder_input)

    if not folder.exists() or not folder.is_dir():
        print("갈!! 경로가 유효하지 않습니다.")
        time.sleep(5)
        return

    image_files = [f for f in folder.iterdir() if f.suffix.lower() in ['.png', '.jpg', '.jpeg', '.webp', '.bmp', '.gif']]

    if not image_files:
        print("갈!!!! 이미지 파일이 없습니다.")
        time.sleep(5)
        return

    # 정렬 기준 설정
    if sort_choice == "1":
        key_func = lambda x: x.name.lower()
    else:
        key_func = lambda x: x.stat().st_mtime

    # 정렬 방향 설정
    reverse = True if order_choice == "2" else False

    # 정렬 적용
    image_files = sorted(image_files, key=key_func, reverse=reverse)

    for i, file in enumerate(image_files, start=1):
        new_name = f"{name_input}_{i:03}{file.suffix.lower()}"
        file.rename(folder / new_name)

    print("이름 변경 완료! 야후~~")
    msgbox.showinfo("완료", "모든 파일 이름 변경이 완료되었습니다!")
    time.sleep(5)

if __name__ == "__main__":
    main()
