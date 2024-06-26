SN = SNnew;

% Додаємо вузли типу "І" для об'єктів
SN = SNaddANDnode(SN, 'Користувач');
SN = SNaddANDnode(SN, 'Клавіатура');
SN = SNaddANDnode(SN, 'Характеристики клавіатури');
SN = SNaddANDnode(SN, 'Потреби та вподобання користувача');

% Додаємо вузли типу "АБО" для атрибутів
SN = SNaddORnode(SN, 'Вік', 'Стать', 'Стиль друку', 'Розмір руки', 'Наявність травм чи захворювань рук');
SN = SNaddORnode(SN, 'Тип перемикачів', 'Підключення', 'Розмір', 'Форма', 'Наявність підставки для зап"ястя', 'Підсвічування');
SN = SNaddORnode(SN, 'Комфорт', 'Продуктивність', 'Ціна', 'Дизайн');

SN = SNaddORnode(SN, 'від 10 до 99', 'Чоловіча', 'Жіноча', 'Зі зором', 'На дотик', 'Маленька', 'Середня', 'Велика', 'Так', 'Ні', 'Механічні', 'Мембранні', 'Через провід', 'Без провіду', 'Повнорозмірна', 'Компактна', 'Пряма', 'Ергономічна', 'Низький', 'Середній', 'Високий', 'Висока', 'Низька', 'Класичний', 'Сучасний', 'Ігровий');

% Додаємо відносини між об'єктами та атрибутами
SN = SNaddrelation(SN, 'Користувач', 'має', 'Вік');
SN = SNaddrelation(SN, 'Користувач', 'має', 'Стать');
SN = SNaddrelation(SN, 'Користувач', 'має', 'Стиль друку');
SN = SNaddrelation(SN, 'Користувач', 'має', 'Розмір руки');
SN = SNaddrelation(SN, 'Користувач', 'має', 'Наявність травм чи захворювань рук');

SN = SNaddrelation(SN, 'Характеристики клавіатури', 'має', 'Тип перемикачів');
SN = SNaddrelation(SN, 'Характеристики клавіатури', 'має', 'Підключення');
SN = SNaddrelation(SN, 'Характеристики клавіатури', 'має', 'Розмір');
SN = SNaddrelation(SN, 'Характеристики клавіатури', 'має', 'Форма');
SN = SNaddrelation(SN, 'Характеристики клавіатури', 'має', 'Наявність підставки для зап"ястя');
SN = SNaddrelation(SN, 'Характеристики клавіатури', 'має', 'Підсвічування');

SN = SNaddrelation(SN, 'Потреби та вподобання користувача', 'визначають', 'Комфорт');
SN = SNaddrelation(SN, 'Потреби та вподобання користувача', 'визначають', 'Продуктивність');
SN = SNaddrelation(SN, 'Потреби та вподобання користувача', 'визначають', 'Ціна');
SN = SNaddrelation(SN, 'Потреби та вподобання користувача', 'визначають', 'Дизайн');

SN = SNaddrelation(SN, 'Вік', 'може бути', 'від 10 до 99');
SN = SNaddrelation(SN, 'Стать', 'може бути', 'Чоловіча');
SN = SNaddrelation(SN, 'Стать', 'може бути', 'Жіноча');
SN = SNaddrelation(SN, 'Стиль друку', 'може бути', 'Зі зором');
SN = SNaddrelation(SN, 'Стиль друку', 'може бути', 'На дотик');
SN = SNaddrelation(SN, 'Розмір руки', 'може бути', 'Маленька');
SN = SNaddrelation(SN, 'Розмір руки', 'може бути', 'Середня');
SN = SNaddrelation(SN, 'Розмір руки', 'може бути', 'Велика');
SN = SNaddrelation(SN, 'Наявність травм чи захворювань рук', 'може бути', 'Так');
SN = SNaddrelation(SN, 'Наявність травм чи захворювань рук', 'може бути', 'Ні');

SN = SNaddrelation(SN, 'Тип перемикачів', 'може бути', 'Механічні');
SN = SNaddrelation(SN, 'Тип перемикачів', 'може бути', 'Мембранні');
SN = SNaddrelation(SN, 'Підключення', 'може бути', 'Через провід');
SN = SNaddrelation(SN, 'Підключення', 'може бути', 'Без провіду');
SN = SNaddrelation(SN, 'Розмір', 'може бути', 'Повнорозмірна');
SN = SNaddrelation(SN, 'Розмір', 'може бути', 'Компактна');
SN = SNaddrelation(SN, 'Форма', 'може бути', 'Пряма');
SN = SNaddrelation(SN, 'Форма', 'може бути', 'Ергономічна');
SN = SNaddrelation(SN, 'Наявність підставки для зап"ястя', 'може бути', 'Так');
SN = SNaddrelation(SN, 'Наявність підставки для зап"ястя', 'може бути', 'Ні');
SN = SNaddrelation(SN, 'Підсвічування', 'може бути', 'Так');
SN = SNaddrelation(SN, 'Підсвічування', 'може бути', 'Ні');

SN = SNaddrelation(SN, 'Комфорт', 'може бути', 'Низький');
SN = SNaddrelation(SN, 'Комфорт', 'може бути', 'Середній');
SN = SNaddrelation(SN, 'Комфорт', 'може бути', 'Високий');
SN = SNaddrelation(SN, 'Продуктивність', 'може бути', 'Низька');
SN = SNaddrelation(SN, 'Продуктивність', 'може бути', 'Середня');
SN = SNaddrelation(SN, 'Продуктивність', 'може бути', 'Висока');
SN = SNaddrelation(SN, 'Ціна', 'може бути', 'Низька');
SN = SNaddrelation(SN, 'Ціна', 'може бути', 'Середня');
SN = SNaddrelation(SN, 'Ціна', 'може бути', 'Висока');
SN = SNaddrelation(SN, 'Дизайн', 'може бути', 'Класичний');
SN = SNaddrelation(SN, 'Дизайн', 'може бути', 'Сучасний');
SN = SNaddrelation(SN, 'Дизайн', 'може бути', 'Ігровий');


SN = SNaddrelation(SN, 'Клавіатура', 'залежить від', 'Користувач');
SN = SNaddrelation(SN, 'Клавіатура', 'залежить від', 'Потреби та вподобання користувача');
SN = SNaddrelation(SN, 'Клавіатура', 'залежить від', 'Характеристики клавіатури');
SN = SNaddrelation(SN, 'Клавіатура', 'залежить від', 'Вік');
SN = SNaddrelation(SN, 'Клавіатура', 'залежить від', 'Стать');
SN = SNaddrelation(SN, 'Клавіатура', 'залежить від', 'Стиль друку');
SN = SNaddrelation(SN, 'Клавіатура', 'залежить від', 'Розмір руки');
SN = SNaddrelation(SN, 'Клавіатура', 'залежить від', 'Наявність травм чи захворювань рук');
SN = SNaddrelation(SN, 'Клавіатура', 'має', 'Тип перемикачів');
SN = SNaddrelation(SN, 'Клавіатура', 'має', 'Підключення');
SN = SNaddrelation(SN, 'Клавіатура', 'має', 'Розмір');
SN = SNaddrelation(SN, 'Клавіатура', 'має', 'Форма');
SN = SNaddrelation(SN, 'Клавіатура', 'має', 'Наявність підставки для зап"ястя');
SN = SNaddrelation(SN, 'Клавіатура', 'має', 'Підсвічування');
SN = SNaddrelation(SN, 'Клавіатура', 'має', 'Комфорт');
SN = SNaddrelation(SN, 'Клавіатура', 'має', 'Продуктивність');
SN = SNaddrelation(SN, 'Клавіатура', 'має', 'Ціна');
SN = SNaddrelation(SN, 'Клавіатура', 'має', 'Дизайн');

% будуємо графічні зображення схеми семантичної мережі
SNplot(SN, 'hierarchy'); % ієрархічне розташування вузлів

figure; % створюємо нове вікно для іншої схеми

SNplot(SN, 'circle'); % кругове розташування вузлів

% створюємо мережу-запит на основі мережі бази знань
SN1=SN;

% видаляємо з мережі-запиту зайві вузли
SN1=SNdelnode(SN1, 'Жіноча', 'Зі зором', 'Маленька', 'Велика', 'Так', 'Мембранні', 'Через провід', 'Компактна', 'Ергономічна', 'Так', 'Ні', 'Низький', 'Середній', 'Низька', 'Середня', 'Низька', 'Висока', 'Класичний', 'Сучасний');
% будуємо графічне зображення схеми мережі-запиту
SNplot(SN1, 'hierarchy'); % випадкове розташування вузлів
% виконуємо запит до семантичної мережі,
% результати якого видаємо на екран
Res=SNfind(SN, SN1)
