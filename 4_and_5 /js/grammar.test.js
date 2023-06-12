import { parse, SyntaxError } from "./grammar";
import { runCmd } from "./turtle";


describe("Test Command Parsing", () => {
  test("Move", () => {
    expect(parse("N 5")).toStrictEqual({ "type": "N", "distance": 5 });
  });
  test("Pen", () => {
    expect(parse("P 4")).toStrictEqual({ "type": "P", "size": 4 });
  });
  test("Press", () => {
    expect(parse("U")).toStrictEqual({ "type": "U" });
  });
  test("Invalid", () => {
    expect(() => { parse("A") }).toThrow(SyntaxError);
  });
});

