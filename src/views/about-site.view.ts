import { makeParagraph, makeLink } from "./views.utils.js";

const PARA_1 = "In this project I'm going to get some practice in for using TS and Python before some interviews next week.";
const PARA_2 = "If you're not already here, Here's a link:";
const LINK_1 = makeLink("#", "HTML Link")

export function makeAboutSiteView() {
    const view = document.createElement('div');

    [PARA_1, PARA_2].forEach((paraText) => {
        const paragraph = makeParagraph(paraText);
        view.appendChild(paragraph);
    });
    
    view.appendChild(LINK_1)

    return view;
}