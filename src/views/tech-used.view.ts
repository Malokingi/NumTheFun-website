import { makeParagraph, makeList } from "./views.utils.js";

const PARA_1 = "Here's a list of the Technology Used for this project:";
const LIST_1 = ['HTML', 'Javascript', 'Typescript', 'Node.js', 'npm', 
    'tsc', 'VSCode', 'Bash', 'Google Chrome'];

export function makeTechUsedView() {
    const view = document.createElement('div');

    view.appendChild(makeParagraph(PARA_1));
    view.appendChild(makeList(LIST_1));
    
    return view;
}
