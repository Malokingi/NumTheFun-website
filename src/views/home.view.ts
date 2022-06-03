import { makeParagraph } from "./views.utils.js";

const PARA_1 = "Hello there, World. Matthew's making a TS Website and integrating a python version of NumTheFun. Stand by...";

export function makeHomeView() {
    const view = document.createElement("div");
  
    const paragraph = makeParagraph(PARA_1);
    view.appendChild(paragraph);
  
    return view;
}