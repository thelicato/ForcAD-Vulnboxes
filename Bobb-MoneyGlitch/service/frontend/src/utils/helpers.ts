export const removeSlash = (v: string): string => {
  return v.replace(/^\/+/, '');
};

export const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));

export const range = (len: number) => Array.from({ length: len }, (_x, i) => i);
export const rangeWithoutZero = (len: number) => Array.from({ length: len - 1 }, (_x, i) => i + 1);

export const capitalize = (s: string): string => {
  return `${s.charAt(0).toUpperCase()}${s.slice(1)}`;
};

export const isObject = (object: Record<any, any>) => {
  return object != null && typeof object === 'object';
};

export const areObjectEquals = (obj1: Record<any, any>, obj2: Record<any, any>) => {
  const props1 = Object.getOwnPropertyNames(obj1);
  const props2 = Object.getOwnPropertyNames(obj2);
  if (props1.length != props2.length) {
    return false;
  }
  for (let i = 0; i < props1.length; i++) {
    const val1 = obj1[props1[i]];
    const val2 = obj2[props1[i]];
    const isObjects = isObject(val1) && isObject(val2);
    if ((isObjects && !areObjectEquals(val1, val2)) || (!isObjects && val1 !== val2)) {
      return false;
    }
  }
  return true;
};
