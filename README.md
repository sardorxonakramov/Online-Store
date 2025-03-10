# Onlineshops

Ushbu loyiha onlayn savdo qilish uchun kichik dastur hisoblanadi.

## Xususiyatlar:
- Foydalanuvchilar email orqali ro'yxatdan o'tishi mumkin.
- Ro'yxatdan o'tgan foydalanuvchilar mahsulotlarni tanlash imkoniyatiga ega.
- Tanlangan mahsulotlar savatchada saqlanadi.
- Admin paneli mavjud bo'lib, mahsulotlarni boshqarish imkoniyati bor.

## O'rnatish
1. Loyihani yuklab oling:
   ```bash
   git clone https://github.com/sardorxonakramov/Onlineshops.git
   cd Onlineshops
   ```
2. Virtual muhitni yarating va faollashtiring:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # MacOS/Linux
   .venv\Scripts\activate     # Windows
   ```
3. Kerakli kutubxonalarni o'rnating:
   ```bash
   pip install -r requirements.txt
   ```
4. Ma'lumotlar bazasini yangilang:
   ```bash
   python manage.py migrate
   ```
5. Serverni ishga tushiring:
   ```bash
   python manage.py runserver
   ```

## Foydalanish
1. Saytga tashrif buyuring: `http://127.0.0.1:8000`
2. Ro'yxatdan o'ting va tizimga kiring.
3. Mahsulotlarni tanlang va savatchaga qo'shing.
4. Xaridni amalga oshiring.

## Hissa qo'shish
Agar siz loyiha ustida ishlashni xohlasangiz, quyidagi bosqichlarni bajaring:
1. Fork qiling.
2. O'zingizning branch-ingizni yarating: `git checkout -b yangi-branch`
3. O'zgarishlarni kiritib commit qiling: `git commit -m "O'zgarish tavsifi"`
4. O'z branch-ingizni push qiling: `git push origin yangi-branch`
5. Pull request jo'nating.

## Muallif
- **Sardorxon Akramov** - [GitHub Profilim](https://github.com/sardorxonakramov)

## Litsenziya
Ushbu loyiha [MIT](LICENSE) litsenziyasi asosida tarqatiladi.

