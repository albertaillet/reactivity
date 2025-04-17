// A minimal reactivity system
const targetMap = new WeakMap();
let activeEffect = null;

export function reactive(obj) {
  return new Proxy(obj, {
    get(target, key) {
      track(target, key);
      return Reflect.get(target, key);
    },
    set(target, key, value) {
      const old = target[key];
      const result = Reflect.set(target, key, value);
      if (old !== value) trigger(target, key);
      return result;
    }
  });
}

export function effect(fn) {
  activeEffect = fn;
  fn(); // run once to collect deps
  activeEffect = null;
}

function track(target, key) {
  if (!activeEffect) return;
  let depsMap = targetMap.get(target);
  if (!depsMap) {
    depsMap = new Map();
    targetMap.set(target, depsMap);
  }
  let dep = depsMap.get(key);
  if (!dep) {
    dep = new Set();
    depsMap.set(key, dep);
  }
  dep.add(activeEffect);
}

function trigger(target, key) {
  const depsMap = targetMap.get(target);
  if (!depsMap) return;
  const dep = depsMap.get(key);
  if (dep) dep.forEach(fn => fn());
}

// A tiny computed helper
export function computed(getter) {
  let value;
  let dirty = true;
  const runner = () => {
    if (dirty) {
      value = getter();
      dirty = false;
    }
    return value;
  };
  effect(() => {
    getter(); // collect deps
    dirty = true;
  });
  return {
    get value() {
      return runner();
    }
  };
}
