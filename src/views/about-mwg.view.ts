import { makeParagraph } from "./views.utils.js";

const PARA_1 = "Matthew got a BS Degree in Computer Science in 2014.";
const PARA_2 = "Here's Matthew's eMail: email_address@domain_name.edu";
const PARA_3 = "Here's Matthew's Phone Number: (867)112-3581";

export function makeAboutMWGView() {
    const view = document.createElement('div');

    [PARA_1, PARA_2, PARA_3].forEach((paraText) => {
        const paragraph = makeParagraph(paraText);
        view.appendChild(paragraph);
      });
    
    return view;
}