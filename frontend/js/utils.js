function injectHtml(id, html) {
  const node = document.getElementById(id);
  if (node) node.innerHTML = html;
}
