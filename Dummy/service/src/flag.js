class FlagService {
    constructor() {
        this.flags = []
    }

    getFlag(id, vuln) {
        return this.flags.find((f) => f.id === id && f.vuln === vuln).flag
    }

    setFlag(id, vuln, flag) {
        const newFlag = {id, vuln, flag}
        this.flags.push(newFlag);
    }

    getLastFlag() {
        const index = this.flags.length-1
        return this.flags[index].flag
    }
}

module.exports = new FlagService();