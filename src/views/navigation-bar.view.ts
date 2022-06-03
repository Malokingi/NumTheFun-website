import { makeAboutMWGView } from "./about-mwg.view.js";
import { makeAboutSiteView } from "./about-site.view.js";
import { makeHomeView } from "./home.view.js";
import { makeTechUsedView } from "./tech-used.view.js";
import { renderView } from "./views.utils.js";

type NavItem = [label: string, viewFn: Function];

const NAV_ITEMS: NavItem[] = [
  ["Home", makeHomeView],
  ["About this site", makeAboutSiteView],
  ["About Matthew", makeAboutMWGView],
  ["Technology used", makeTechUsedView],
];

export function makeNavView() {
    const wrapper = document.createElement("div");
  
    NAV_ITEMS.forEach((navItem) => {
      const navLink = makeNavLink(...navItem);
      wrapper.appendChild(navLink);
    });

    return wrapper;
}

function makeNavLink(label: string, viewFn: Function) {
    const link = document.createElement("a");

    link.textContent = label;
    link.addEventListener("click", handleNavClick(viewFn));
    link.setAttribute("style", "padding: 2px; text-decoration: underline;");

    return link;
}

function handleNavClick(viewFn: Function) {
    return function (event: MouseEvent) {
        event.preventDefault();
        renderView(viewFn());
    };
}
