import { parse, SyntaxError } from "./grammar";
import { runCmd } from "./turtle";



describe("Test Command Execution", () => {
  test("doMove", () => {
    expect(runCmd({ "type": "N", "distance": 5 })).toStrictEqual("doMove");
  });
  test("doPress", () => {
    expect(runCmd({ "type": "U" })).toStrictEqual("doPress");
  });
  test("doSelect", () => {
    expect(runCmd({ "type": "P", "size": 55 })).toStrictEqual("doSelect");
  });

});
