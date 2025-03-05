import os
import shutil


def organize_files(directory):
    if not os.path.exists(directory):
        print("Belirtilen klasör bulunamadı!")
        return

    categories = {
        "Resimler": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
        "Belgeler": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        "Videolar": [".mp4", ".mov", ".avi", ".mkv"],
        "Müzikler": [".mp3", ".wav", ".aac", ".flac"],
        "Arşivler": [".zip", ".rar", ".tar", ".gz"],
        "Diğer": []
    }

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1].lower()
            moved = False

            for category, extensions in categories.items():
                if file_ext in extensions:
                    category_path = os.path.join(directory, category)
                    if not os.path.exists(category_path):
                        os.makedirs(category_path)
                    shutil.move(file_path, os.path.join(category_path, file))
                    moved = True
                    break

            if not moved:  # Eğer dosya belirli bir kategoriye uymuyorsa "Diğer" klasörüne taşı
                other_path = os.path.join(directory, "Diğer")
                if not os.path.exists(other_path):
                    os.makedirs(other_path)
                shutil.move(file_path, os.path.join(other_path, file))

    print("Dosyalar başarıyla düzenlendi!")


if __name__ == "__main__":
    folder_path = input("Düzenlemek istediğiniz klasörün yolunu girin: ")
    organize_files(folder_path)
