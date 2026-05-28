import { Application, Controller } from "https://unpkg.com/@hotwired/stimulus/dist/stimulus.js";

const application = Application.start();

application.register(
  "auth",
  class extends Controller {
    static targets = ["status"];

    connect() {
      if (this.hasStatusTarget) {
        this.statusTarget.textContent = "Stimulus connected.";
      }
    }
  }
);
