import g4f
from googletrans import Translator


def translate_to_kazakh(title, subtitle):
    """
    Переводит заголовок (title) и подзаголовок (subtitle) на казахский язык с помощью g4f.
    Также генерирует пролог на казахском языке.
    """
    prompt = (
        f"Translate the following title and subtitle into Kazakh, and create a prologue in Kazakh based on them. Very Very Important don't use a paragraph for write Prologue make it solid:\n \n"
        f"Title: {title}\nSubtitle: {subtitle}\n\n"
        f"Response format:\n"
        f"Title (Kazakh): <translated_title>"
        f"Subtitle (Kazakh): <translated_subtitle>"
        f"Prologue (Kazakh): <generated_prologue>"
    )
    response = g4f.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    
    # Проверка типа ответа
    if isinstance(response, str):
        translated_text = response
    elif isinstance(response, dict):
        translated_text = response.get('choices', [{}])[0].get('message', {}).get('content', '')
    else:
        raise ValueError("Unexpected response format from g4f")

    # Парсинг текста
    lines = translated_text.split("\n")
    try:
        title_kz = lines[0].replace("Title (Kazakh):", "").strip()
        subtitle_kz = lines[1].replace("Subtitle (Kazakh):", "").strip()
        prologue_kz = lines[2].replace("Prologue (Kazakh):", "").strip()

        print('qqqq', lines)
    except IndexError:
        title_kz, subtitle_kz, prologue_kz = None, None, None

    return title_kz, subtitle_kz, prologue_kz



def split_text_by_paragraphs(text, max_chars=10000):
    """
    Разделяет текст на части по абзацам, где каждая часть не превышает max_chars символов.
    """
    paragraphs = text.split('/n')  # Разделение по абзацам
    parts = []
    current_part = ""
    
    for paragraph in paragraphs:
        if len(current_part) + len(paragraph) + 1 <= max_chars:
            current_part += paragraph + "\n"
        else:
            parts.append(current_part.strip())
            current_part = paragraph + "\n"
    
    if current_part:
        parts.append(current_part.strip())
    
    return parts



def translate_large_text(text):
    """
    Переводит большой текст, разбивая его на части.
    """
    parts = split_text_by_paragraphs(text)
    translated_parts = []
    i = 0
    for part in parts:
        print(f"Translating part {i + 1}/{len(parts)}...")
        if part != '' and part != None:
            print('parttt', part)
            prompt = (
                f'Translate the following text into Kazakh without hello.Sometimes I might give something like "Your browser does not support the audio element" that are not related to the text, in such cases give empty answers :\n\n'
                f"{part}\n\n"
                f"Response format:\n<translated_text>"
            )
            response = g4f.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )
        else:
            i += 1
            continue
        # Обработка ответа
        if isinstance(response, str):
            translated_text = response
        elif isinstance(response, dict):
            translated_text = response.get('choices', [{}])[0].get('message', {}).get('content', '')
        else:
            raise ValueError("Unexpected response format from g4f")
        print('translated_text', translated_text.strip())
        translated_parts.append(translated_text.strip())
        print('translated_parts', translated_parts)
        i += 1
    return "\n\n".join(translated_parts)





def split_text_into_chunks(text, max_length=5000):
    # Разбивает текст на части не более max_length символов
    chunks = []
    if len(text) < max_length:
        return text
    while len(text) > max_length:
        split_index = text[:max_length].rfind("\n\n") 
        if split_index == -1:
            split_index = max_length
        chunks.append(text[:split_index])
        text = text[split_index:]
    print(len(text))
    chunks.append(text)
    return chunks

async def translate_text_to_kazakh(text):
    new_text_list = split_text_by_paragraphs(text)

    translations = []
    translator = Translator()
    for row in new_text_list:
        print('row', len(row))
        translated = await translator.translate(row, src='auto', dest='kk')

        translations.append(translated.text)
    translated_text = " ".join(translations)
    # print(translated_text)
    return translated_text
