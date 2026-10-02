def validate_phone(phone: str) -> bool:
    """Валидация российских номеров телефона."""
    import re
    pattern = r'^(\+7|8)[\s\-]?\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}$'
    return bool(re.match(pattern, phone))