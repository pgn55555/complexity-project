# Задача о деревенском почтальоне (RURAL POSTMAN, RPP)

Задача о деревенском почтальоне заключается в том, чтобы в графе с некоторым подмножеством рёбер найти цикл минимального суммарного веса, хотя бы один раз проходящий через каждое ребро из данного подмножества. В этой статье будет доказано, что эта задача является NP-полной, будет доказана полиномиальная разрешимость в особом случае графа, а также имплементирован алгоритм для решения задачи в этом случае.

Текст работы: [text.pdf](text.pdf)

Тесты запускаются командой:

    pytest tests.py