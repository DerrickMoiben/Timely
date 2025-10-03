# Timely  

Timely is a **booking and mini-website builder platform** for small businesses such as car washes, spas, salons, and barbershops.  
It allows business owners to create a custom mini-site, showcase their services, set working hours, and allow customers to book visits online.  

---

## 🚀 Project Vision  
Timely is built to help **local businesses** digitize their operations with minimal effort.  

A business owner can:  
1. Start a journey on Timely by choosing their **business type**.  
2. Answer **guided onboarding questions** (specific to their industry).  
3. Get a ready-to-use **mini website** with booking functionality.  
4. Manage bookings and customers from their dashboard.  

Later, businesses will also be able to:  
- Use **custom subdomains/domains**.  
- Accept **online payments** (M-Pesa, cards, etc.).  
- Receive **notifications** via SMS/email.  

---

## 🛠️ Tech Stack  
- **Backend**: Django + Django REST Framework (later for APIs)  
- **Frontend**: Django templates + HTMX (for MVP), React (future version)  
- **Database**: PostgreSQL  
- **Styling**: Tailwind CSS (or Bootstrap for fast prototyping)  
- **Notifications**: Email (Django built-in) / SMS (Africa’s Talking, Twilio)  

---

## 📊 Core Models (MVP)  

- **BusinessType**: Defines industries (Car Wash, Spa, Salon, Barber, etc.).  
- **Question**: Onboarding questions linked to business type.  
- **QuestionOption**: Options for multiple-choice questions.  
- **Business**: Stores business info (name, type, subdomain, owner).  
- **Service**: List of services offered by the business.  
- **Booking**: Customer bookings (name, phone, time, status).  
- **BusinessAnswer**: Stores onboarding answers for each business.  

---

## 🔄 Onboarding Flow  

1. Visitor clicks **“Start with Timely”** on homepage.  
2. Step 1: Select **Business Type**.  
3. Step 2: Answer **business-specific questions**  
   - e.g., for Car Wash → working hours, packages.  
   - e.g., for Spa → services offered, duration, price.  
4. Step 3: Add general info (business name, contact, logo).  
5. Step 4: Preview and **publish site** → available at `/b/{subdomain}/`.  

All steps are handled dynamically using **HTMX** (no full-page reloads).  

---

## 📦 Features (MVP)  

✅ Business onboarding wizard  
✅ Auto-generated mini-site for each business  
✅ Booking system for customers  
✅ Owner dashboard to manage bookings  

---

## 🚧 Roadmap  

### Phase 1 – MVP (Django + HTMX)  
- Guided onboarding (dynamic forms per business type).  
- Auto-generated site at `/b/{subdomain}/`.  
- Customer bookings with dashboard.  

### Phase 2 – Enhanced Features  
- Payments integration (M-Pesa, Stripe, PayPal).  
- SMS/email notifications.  
- Subdomain + custom domain support.  

### Phase 3 – Full Product  
- API-first with Django REST Framework.  
- React frontend with customization options.  
- Theming (colors, logos, images).  

---

## ⚡ Getting Started (for Devs)  

```bash
# Clone repo
git clone https://github.com/yourusername/timely.git
cd timely

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
