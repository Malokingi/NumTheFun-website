/**
 * Here are some functions to be shared among 
 * the other files in src/views
 */

export function makeParagraph(text: string) {
    const paragraph = document.createElement('p');
    paragraph.textContent = text;

    return paragraph;
}

export function makeLink(address: string, link_text: string, newTab = false) {
    const link = document.createElement('a');
    link.href = address;
    link.textContent = link_text;
    if (newTab){
        link.target = '_blank';
    }

    return link;
}

export function makeList(list_items: string[], ordered = false) {
    const list_type = ordered ? 'ol' : 'ul'
    const list = document.createElement(list_type);

    list_items.forEach((item_text) => {
        const list_item = document.createElement('li');
        list_item.textContent = item_text;
        list.appendChild(list_item);
    });

    return list;
}

export function renderView(view: HTMLElement) {
    const wrapper = clearMainWrapper();
    wrapper?.appendChild(view);
}

function clearMainWrapper() {
    const wrapper = document.getElementById("section-content");
    wrapper?.childNodes.forEach((childNode) => {
      wrapper.removeChild(childNode);
    });
    return wrapper;
}
