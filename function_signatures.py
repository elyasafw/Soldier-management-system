# ============================================================
# קובץ חלוקת פונקציות — מערכת ניהול תורנויות חיילים
# ============================================================


# ────────────────────────────────────────────────────────────
# utils.py
# ────────────────────────────────────────────────────────────

def find_soldier_by_id(soldier_id: int) -> dict | None:
    """
    נתיב: utils.py
    קלט: soldier_id (int) — מספר אישי
    פעולה: מחפשת חייל ברשימת החיילים לפי מספר אישי
    מחזירה: מילון החייל אם נמצא, None אם לא נמצא
    """
    pass

def is_valid_name(name: str) -> bool:
    """
    נתיב: utils.py
    קלט: name (str) — שם לבדיקה
    פעולה: בודקת האם השם אינו ריק ואינו מכיל רק רווחים
    מחזירה: True אם השם תקין, False אחרת
    """
    pass

def is_valid_status(status: str) -> bool:
    """
    נתיב: utils.py
    קלט: status (str) — סטטוס לבדיקה
    פעולה: בודקת האם הסטטוס הוא אחד מ: "pending", "completed", "missed"
    מחזירה: True אם הסטטוס חוקי, False אחרת
    """
    pass

def is_valid_day(day: str) -> bool:
    """
    נתיב: utils.py
    קלט: day (str) — יום לבדיקה
    פעולה: בודקת האם היום הוא אחד מ: sunday, monday, tuesday, wednesday, thursday
           ימי שישי ושבת אסורים
    מחזירה: True אם היום חוקי, False אחרת
    """
    pass


# ────────────────────────────────────────────────────────────
# soldier_manager.py
# ────────────────────────────────────────────────────────────

def add_soldier(soldier_id: int, name: str) -> None:
    """
    נתיב: soldier_manager.py
    קלט: soldier_id (int) — מספר אישי, name (str) — שם החייל
    פעולה: מוסיפה חייל חדש לרשימת החיילים
    מחזירה: None
    זורקת: ValueError אם המספר האישי כבר קיים או אם השם ריק
    """
    pass

def remove_soldier(soldier_id: int) -> None:
    """
    נתיב: soldier_manager.py
    קלט: soldier_id (int) — מספר אישי של החייל להסרה
    פעולה: מסירה את החייל מרשימת החיילים
    מחזירה: None
    זורקת: KeyError אם החייל לא קיים במערכת
    """
    pass

def get_all_soldiers() -> list:
    """
    נתיב: soldier_manager.py
    קלט: אין
    פעולה: שולפת את רשימת כל החיילים הרשומים במערכת
    מחזירה: רשימה של כל מילוני החיילים
    """
    pass


# ────────────────────────────────────────────────────────────
# duty_manager.py
# ────────────────────────────────────────────────────────────

def add_duty(soldier_id: int, duty_name: str, day: str) -> None:
    """
    נתיב: duty_manager.py
    קלט: soldier_id (int) — מספר אישי, duty_name (str) — שם התורנות, day (str) — יום
    פעולה: מוסיפה תורנות לחייל עם סטטוס התחלתי "pending"
    מחזירה: None
    זורקת: KeyError אם החייל לא קיים
             ValueError אם כבר קיימת תורנות עם אותו שם, או שהיום לא חוקי
    """
    pass

def update_duty_status(soldier_id: int, duty_name: str, new_status: str) -> None:
    """
    נתיב: duty_manager.py
    קלט: soldier_id (int) — מספר אישי, duty_name (str) — שם התורנות,
          new_status (str) — הסטטוס החדש
    פעולה: מעדכנת את סטטוס התורנות של החייל
    מחזירה: None
    זורקת: KeyError אם החייל לא קיים או התורנות לא נמצאה
             ValueError אם הסטטוס לא חוקי
    """
    pass

def get_soldier_duties(soldier_id: int) -> list:
    """
    נתיב: duty_manager.py
    קלט: soldier_id (int) — מספר אישי
    פעולה: שולפת את רשימת התורנויות של חייל מסוים
    מחזירה: רשימה של מילוני תורנויות של אותו חייל
    זורקת: KeyError אם החייל לא קיים
    """
    pass


# ────────────────────────────────────────────────────────────
# main.py
# ────────────────────────────────────────────────────────────

def main() -> None:
    """
    נתיב: main.py
    קלט: אין
    פעולה: מריצה את לולאת התפריט הראשית — מציגה אפשרויות, קוראת בחירה,
           ומפנה לפונקציית handle המתאימה
    מחזירה: None
    """
    pass

def handle_add_soldier() -> None:
    """
    נתיב: main.py
    קלט: אין (קוראת input מהמשתמש בפנים)
    פעולה: מבקשת מספר אישי ושם, קוראת ל-add_soldier, מציגה הודעת הצלחה/שגיאה
    מחזירה: None
    """
    pass

def handle_remove_soldier() -> None:
    """
    נתיב: main.py
    קלט: אין (קוראת input מהמשתמש בפנים)
    פעולה: מבקשת מספר אישי, קוראת ל-remove_soldier, מציגה הודעת הצלחה/שגיאה
    מחזירה: None
    """
    pass

def handle_view_soldiers() -> None:
    """
    נתיב: main.py
    קלט: אין
    פעולה: קוראת ל-get_all_soldiers ומדפיסה את כל החיילים הרשומים
    מחזירה: None
    """
    pass

def handle_add_duty() -> None:
    """
    נתיב: main.py
    קלט: אין (קוראת input מהמשתמש בפנים)
    פעולה: מבקשת מספר אישי, שם תורנות ויום, קוראת ל-add_duty, מציגה הודעת הצלחה/שגיאה
    מחזירה: None
    """
    pass

def handle_update_status() -> None:
    """
    נתיב: main.py
    קלט: אין (קוראת input מהמשתמש בפנים)
    פעולה: מבקשת מספר אישי, שם תורנות וסטטוס חדש, קוראת ל-update_duty_status,
           מציגה הודעת הצלחה/שגיאה
    מחזירה: None
    """
    pass

def handle_view_duties() -> None:
    """
    נתיב: main.py
    קלט: אין (קוראת input מהמשתמש בפנים)
    פעולה: מבקשת מספר אישי, קוראת ל-get_soldier_duties, מדפיסה את התורנויות
    מחזירה: None
    """
    pass