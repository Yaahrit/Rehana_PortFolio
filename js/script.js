//Update the current year in the footer
document.getElementById("current-year").textContent = new Date().getFullYear();
// Scroll to Top Button
const scrollBtn = document.getElementById("scrollTopBtn");

window.onscroll = () => {
  scrollBtn.style.display = window.scrollY > 200 ? "block" : "none";
};

scrollBtn.onclick = () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
};

// Initialize AOS (Animate On Scroll) library
const swiper = new Swiper(".mySwiper", {
  slidesPerView: 1,
  spaceBetween: 20,
  loop: true,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    576: {
      slidesPerView: 1,
    },
    768: {
      slidesPerView: 2,
    },
    992: {
      slidesPerView: 3,
    },
  },
});

document.querySelector("#contactForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const data = {
    name: document.getElementById("name").value,
    email: document.getElementById("email").value,
    message: document.getElementById("message").value
  };

  const res = await fetch("http://127.0.0.1:5000/contact", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });

  const result = await res.json();
  alert(result.message);
});