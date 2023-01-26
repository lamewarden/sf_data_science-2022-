# Project 1. Анализ вакансий с hh.ru

## 1. Project description

Компания Booking хочет найти способ наказывать отели, накручивающие себе рейтинг. 
Чтобы определять такие отели, компания хочет обучить random forest модель для 
предстказания рейтинга модели по остальным параметрам. Если рейтинг конкретного отеля сильно 
отличается о результата, то, возможно, отель ведёт себя нечестно, и его стоит проверить.

## 2. Task
Очистить и подготовить данные для работы соответствующей модели.
## 3. Data description
[Таблица](https://drive.google.com/file/d/1Qj0iYEbD64eVAaaBylJeIi3qvMzxf2C_/view?usp=sharing)
С колонками:
- `hotel_address` — адрес отеля;
    
- `review_date` — дата, когда рецензент разместил соответствующий отзыв;
    
- `average_score` — средний балл отеля, рассчитанный на основе последнего комментария за последний год;
    
- `hotel_name` — название отеля;
    
- `reviewer_nationality` — страна рецензента;
    
- `negative_review` — отрицательный отзыв, который рецензент дал отелю;
    
- `review_total_negative_word_counts` — общее количество слов в отрицательном отзыв;
    
- `positive_review` — положительный отзыв, который рецензент дал отелю;
    
- `review_total_positive_word_counts` — общее количество слов в положительном отзыве.
    
- `reviewer_score` — оценка, которую рецензент поставил отелю на основе своего опыта;
    
- `total_number_of_reviews_reviewer_has_given` — количество отзывов, которые рецензенты дали в прошлом;
    
- `total_number_of_reviews` — общее количество действительных отзывов об отеле;
    
- `tags` — теги, которые рецензент дал отелю;
    
- `days_since_review` — количество дней между датой проверки и датой очистки;
    
- `additional_number_of_scoring` — есть также некоторые гости, которые просто поставили оценку сервису, но не оставили отзыв. Это число указывает, сколько там действительных оценок без проверки.
    
- `lat` — географическая широта отеля;
    
- `lng` — географическая долгота отеля.

## 4. Project steps
- Заполнение пропусков;
- Выделение новых признаков;
- Кодирование;
- Оценка и фильтрация важных для модели признаков.

## 5. Results
- Таблица данных, подготовленных для участия в [соревновании на kaggle](https://www.kaggle.com/competitions/sf-booking)

## 6. Conclusions
Данные подготовлены. Хотелось бы еще улучшить результаты метрики, но добавление даже потенциально полезных признаков (расстояние до центра города и тд) только ухудшало метрику.
