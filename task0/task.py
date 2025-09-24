import csv
import sys


def main():
    if len(sys.argv) < 2:
        print("Ошибка: Укажите путь к CSV файлу")
        print("Использование: python task.py <путь_к_csv_файлу>")
        return []

    csv_file_path = sys.argv[1]

    try:
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            edges = [row for row in reader if len(row) >= 2 and row[0].strip() and row[1].strip()]

        if not edges:
            return []

        all_vertices = set()
        for edge in edges:
            all_vertices.add(int(edge[0].strip()))
            all_vertices.add(int(edge[1].strip()))

        vertices = sorted(all_vertices)
        n = len(vertices)
        vertex_to_index = {vertex: idx for idx, vertex in enumerate(vertices)}

        adjacency_matrix = [[0] * n for _ in range(n)]

        for edge in edges:
            i = vertex_to_index[int(edge[0].strip())]
            j = vertex_to_index[int(edge[1].strip())]
            adjacency_matrix[i][j] = 1
            adjacency_matrix[j][i] = 1

        return adjacency_matrix

    except FileNotFoundError:
        print(f"Ошибка: Файл '{csv_file_path}' не найден")
        return []
    except Exception as e:
        print(f"Ошибка при обработке файла: {e}")
        return []


if __name__ == "__main__":
    result = main()
    for row in result:
        print(row)