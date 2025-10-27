export function splitLines(value: string): string[] {
  return value
    .split(/\r?\n/u)
    .map((line) => line.trim())
    .filter((line) => line.length > 0);
}

export function joinLines(values: string[] | undefined | null): string {
  if (!values || values.length === 0) {
    return "";
  }
  return values
    .map((line) => line.trim())
    .filter((line) => line.length > 0)
    .join("\n");
}
