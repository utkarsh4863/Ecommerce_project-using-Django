# 🛍️ Django E-commerce Platform

A modern, feature-rich e-commerce platform built with **Django** and **Python**. ShoppinglyX provides a complete online shopping experience with product management, user authentication, shopping cart functionality, and seamless order processing.

## ✨ Features

### User Authentication & Authorization
- User registration and login with secure password management
- User profile management and account customization

### Product Management
- Browse products by categories and search functionality
- Product filtering, detailed descriptions, and image galleries
- Real-time inventory management

### Shopping Cart
- Add/remove items with quantity management
- Real-time cart updates and price calculation
- Persistent cart storage

### Order Management
- Streamlined checkout process
- Complete order history and tracking
- Payment integration ready for production

### Admin Panel
- Django admin interface for complete control
- Product, order, and user management dashboards

## 🛠️ Tech Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.x | Backend language |
| Django | 3.1.5 | Web framework |
| Pillow | 8.1.0 | Image processing |
| SQLite/PostgreSQL | Latest | Database |
| asgiref | 3.3.1 | ASGI support |
| pytz | 2020.5 | Timezone support |
| sqlparse | 0.4.1 | SQL parsing |

## 🚀 Quick Start

**Clone the repository:**
```bash
git clone https://github.com/utkarsh4863/Ecommerce_project-using-Django.git
cd Ecommerce_project-using-Django
```

**Setup environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**Configure & Run:**
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to access the application.

## ⚙️ Configuration

Create a `.env` file in the root directory:
```
DEBUG=True
SECRET_KEY=your_secret_key_here
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
```

## 🔗 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/products/` | GET | List all products |
| `/api/products/<id>/` | GET | Retrieve product details |
| `/api/cart/` | GET/POST | View or update cart |
| `/api/orders/` | GET/POST | List or create orders |

## 🗄️ Core Database Models

- **User** – Default Django User model with extended profile
- **Customer** – Extended profile with address and contact information
- **Product** – Product details, images, pricing, and category
- **Cart** – User shopping cart with product and quantity tracking
- **Order** – Order history with status and timestamps

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/YourFeature`
3. Commit changes: `git commit -m 'Add feature'`
4. Push to branch: `git push origin feature/YourFeature`
5. Create a Pull Request

## 📄 License

This project is open source and available under the MIT License.

---

**Happy Shopping! 🎉**

