import { Statistic } from './Statistic'

export type AddNewStatistic = Omit<Statistic, '_id' | 'date'>
