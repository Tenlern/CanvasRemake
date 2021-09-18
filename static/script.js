// Инициализация рабочего пространства
let cy = cytoscape({
  container: document.getElementById('cy'), // container to render in

   // interaction options:
  minZoom: 1e-50,
  maxZoom: 1e50,
  zoomingEnabled: true,
  userZoomingEnabled: true,
  panningEnabled: true,
  userPanningEnabled: true,
  boxSelectionEnabled: true,
  selectionType: 'single',
  touchTapThreshold: 8,
  desktopTapThreshold: 4,
  autolock: false,
  autoungrabify: false,
  autounselectify: false,

  // rendering options:
  headless: false,
  styleEnabled: true,
  hideEdgesOnViewport: false,
  textureOnViewport: false,
  motionBlur: false,
  motionBlurOpacity: 0.2,
  wheelSensitivity: 1,
  pixelRatio: 'auto'
});

// При нажатии на правую кнопку мышки создаем новый узел
cy.on('cxttap', function (event) {
  let node = cy.add({
    group: 'nodes',
    data: { weight: 75 },
    position: {
      x: event.position.x,
      y: event.position.y,}
  })

  fetch('/node', {
    method: "POST",
    headers: new Headers(),
    body: {
      id: node.id,
      position: node.position,
    }
  }).then(function (response) {
    console.log(response)
  })
});