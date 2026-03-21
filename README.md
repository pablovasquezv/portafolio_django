# 🌐 Mi Portfolio Digital con DJANGO.

<div align="center">

**Un portafolio virtual moderno, responsivo y profesional para destacar mis proyectos de trabajos.**

[🚀 Ver Demo](#) | 📄 Documentación | 💡 Contribuir

</div>

***

## 📖 Descripción

Este proyecto es un **Portfolio Virtual** diseñado para presentar de manera impactante todas mis habilidades, proyectos y experiencia profesional. Construido con las mejores prácticas de desarrollo web, ofrece una experiencia de usuario fluida, totalmente responsiva (móvil, tablet y escritorio) y optimizada para motores de búsqueda (SEO).

### ✨ Características Principales
- 🎨 **Diseño Moderno**: Interfaz limpia y estética gracias a Bootstrap.
- ⚡ **Alto Rendimiento**: Optimización de carga y scripts eficientes.
- 📱 **100% Responsivo**: Se adapta a cualquier dispositivo.
- 🌍 **Multilenguaje**: Estructura preparada para internacionalización.
- 🔌 **Extensible**: Fácil integración con CMS o APIs externas.

***

## 🛠️ Tecnologías Utilizadas

El proyecto se basa en un stack tecnológico robusto y ampliamente adoptado:

| Categoría | Tecnologías |
|-----------|-------------|
| 🏗️ **Estructura** | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" width="20"/> **HTML5** |
| 🎨 **Estilos** | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" width="20"/> **CSS3** <br> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-original.svg" width="20"/> **Bootstrap 5** |
| ⚙️ **Lógica Frontend** | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="20"/> **JavaScript (ES6+)** |
| 🐍 **Backend** | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="20"/> **Python** <br> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-original.svg" width="20"/> **Django** |

***

## 📋 Prerrequisitos

Para ejecutar este proyecto **localmente**, asegúrate de tener instalados los siguientes componentes (mínimo):

1. **Node.js** (v14 o superior) - *Opcional, para compilar assets*
2. **Python** (v3.8 o superior)
3. **Git**
4. Un editor de código (Recomendado: [VS Code](https://code.visualstudio.com/))

***

## 🚀 Instalación y Configuración

Sigue estos pasos para clonar y ejecutar el proyecto en tu entorno local:

### 1. Clonar el repositorio
```bash
git clone https://github.com/pablovasquezv/portafolio_django.git
cd portfolio-website
```

### 2. Configuración del Entorno Virtual (Backend)
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependencias de Django
pip install -r requirements.txt
```

### 3. Configuración de Variables de Entorno
Crea un archivo `.env` en la raíz y define:
```env
SECRET_KEY=tu-clave-secreta
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 4. Migraciones y Superusuario
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 5. Ejecutar el Servidor
```bash
# Backend (Django)
python manage.py runserver

# Frontend (Si usas compilación de assets)
npm start  # o el comando correspondiente
```

🌐 Abre tu navegador en: `http://127.0.0.1:8000`

***

## 📂 Estructura del Proyecto

```
portfolio-website/
├── static/              # Archivos estáticos (CSS, JS, Imágenes)
├── templates/           # Plantillas HTML
├── portfolio/           # App principal de Django
│   ├── models.py        # Modelos de datos
│   ├── views.py         # Lógica de negocio
│   └── urls.py          # Rutas
├── requirements.txt     # Dependencias de Python
├── manage.py            # Script de gestión de Django
└── README.md            # Este archivo
```

***

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Si deseas mejorar el proyecto:

1. Fork el repositorio 🍴
2. Crea tu rama de característica (`git checkout -b feature/AmazingFeature`) 🌿
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`) ✅
4. Push a la rama (`git push origin feature/AmazingFeature`) 🚀
5. Abre un Pull Request 🔄

***

## 📝 Changelog

| Fecha | Autor | Cambios Realizados |
| :--- | :--- | :--- |
| 19-02-2024 | **Juan Pablo Váquez** | 🎉 Inicialización del proyecto, estructura base y documentación. |
| 20-03-2026 | **Juan Pablo Váquez** | ✨ Mejora profesional del README, adición de iconos y tablas. |

***

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**. Ver el archivo [LICENSE](LICENSE) para más detalles.

***

<div align="center">

**Hecho con ❤️ y tecnología open source**

⭐ ¡Si este proyecto te ayudó, considera darle una estrella!

</div>

***

## **📱 COMO USARLO:**

1. **Copiar** todo el contenido
2. **Crear** `README.md` en raíz del proyecto
3. **Pegar** → `Ctrl + S`
4. **Subir** a GitHub → **README renderizado hermoso** 🎉


***

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para reportar bugs o sugerir mejoras. Envía pull requests para colaborar con nuevas funcionalidades o correcciones.

***

## 👨‍💻 Autor

**Juan Pablo Vásquez** – Proyecto desarrollado y mantenido.
**Pablo** - [LinkedIn](https://www.linkedin.com/in/juan-pablo-vasquez-vasquez-8a9693206)  
**Email**: vasquezsoftwaresolutions.com

***

<div align="center">

#### Última actualización  
*Juan Pablo Vásquez* - 20-03-2026
</div>
