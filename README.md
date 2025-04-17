# Reactivity

This repo explores different reactive programming libraries in JavaScript.

The same simple reactive app is implmented with multiple different reactive web libraries.
This is learning experience for understanding different APIs for reactivity in JavaScript.

The libraries used are:

- [Vue 3](/vue.html)
- [SolidJS](/solid.html)
- [AlpineJS](/alpine.html)
- [Standalone reactive](/reactive.html) implementation in [/reactive.js](./reactive.js)

## Running the examples

To run the examples, clone this repo and run the following commands:

Fetch the data from the API and save it to a local sqlite database.

```bash
./fetch_data.sh
```

Start the server on localhost (both serving the static HTML file and the API)

```bash
./server.py
```

## References:

### Libraries

- [vue](https://vuejs.org)
  - [Vue reactivity documentation](https://vuejs.org/api/reactivity-core.html)
  - [@vue/reactivity](https://github.com/vuejs/core/tree/main/packages/reactivity).
    The implementation of this module is inspired by the following prior art in the JavaScript ecosystem:
    - [Meteor Tracker](https://docs.meteor.com/api/tracker.html)
    - [nx-js/observer-util](https://github.com/nx-js/observer-util)
    - [salesforce/observable-membrane](https://github.com/salesforce/observable-membrane)
- [react](https://reactjs.org)
- [svelte](https://svelte.dev)
  - [ractivejs](https://github.com/ractivejs/ractive)
- [preact](https://preactjs.com)
  - [preact/signals-core](https://preactjs.com/guide/v10/signals/) [Preact signals guide](https://preactjs.com/guide/v10/signals/)
- [solidjs](https://solidjs.com)
  - [@solid/react](https://solidjs.com/docs/api#reactivity)
- [snabbdom](https://github.com/snabbdom/snabbdom) (was the basis for Vue 2 virtual DOM)
- [mithril](https://mithril.js.org)
- [lit](https://lit.dev)
- [alpinejs](https://alpinejs.dev)
- [reef](https://github.com/cferdinandi/reef)

### Only-reactivity libraries

- [@vue/reactivity](https://github.com/vuejs/core/tree/main/packages/reactivity).
- [@preact/signals-core](https://github.com/preactjs/signals)
- [rxjs](https://rxjs.dev) [repo](https://github.com/ReactiveX/rxjs) (has a log of npm downloads)
- [baconjs](https://baconjs.github.io) [repo](https://github.com/baconjs/bacon.js)
- [mobx](https://mobx.js.org) (unclear README)
- [cycle.js](https://cycle.js.org) [repo](https://github.com/cyclejs/cyclejs)
- [most](http://mostcore.readthedocs.io) [repo][https://github.com/cujojs/most]
- [valtio](https://github.com/pmndrs/valtio)
- [kefir](https://kefirjs.github.io/kefir/) [repo](https://github.com/kefirjs/kefir)
- [maverick-js/signals](https://github.com/maverick-js/signals)
- [hyperactiv](https://github.com/elbywan/hyperactiv)
- [statin](https://github.com/tomasklaen/statin)
- Apparently there are a [LOT more](https://xgrommx.github.io/rx-book/content/resources/reactive_libraries/index.html)

### Reference blog post

- [byby.dev](https://byby.dev/js-reactive-libraries) JavaScript Reactive Programming Libraries
