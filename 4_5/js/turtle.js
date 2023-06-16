export const runCmd = (cmd) => {
    const CMDS = new Map([
        ["P",(command)=>{return "doSelect"}],
        ["U",(command)=>{return "doPress"}],
        ["D",(command)=>{return "doPress"}],
        ["N",(command)=>{return "doMove"}],
        ["S",(command)=>{return "doMove"}],
        ["E",(command)=>{return "doMove"}],
        ["W",(command)=>{return "doMove"}],
    ]);
    return CMDS.get(cmd.type)(cmd);
};

